import Foundation
import EventKit

// Usage: swift cal-read.swift YYYY-MM-DD YYYY-MM-DD
// Prints events in the given date range, including recurring event instances.

let args = CommandLine.arguments
let fmt = DateFormatter()
fmt.dateFormat = "yyyy-MM-dd"
fmt.timeZone = TimeZone.current

let today = Calendar.current.startOfDay(for: Date())
let startDate: Date
let endDate: Date

if args.count >= 3, let s = fmt.date(from: args[1]), let e = fmt.date(from: args[2]) {
    startDate = s
    endDate = Calendar.current.date(bySettingHour: 23, minute: 59, second: 59, of: e) ?? e
} else {
    startDate = today
    endDate = Calendar.current.date(byAdding: .day, value: 7, to: today) ?? today
}

let store = EKEventStore()
let sema = DispatchSemaphore(value: 0)

store.requestFullAccessToEvents { granted, error in
    defer { sema.signal() }
    guard granted else {
        fputs("error: Calendar access denied\n", stderr)
        return
    }

    let calendars = store.calendars(for: .event)
    let predicate = store.predicateForEvents(withStart: startDate, end: endDate, calendars: calendars)
    let events = store.events(matching: predicate)

    let outFmt = DateFormatter()
    outFmt.dateFormat = "EEEE, MMMM d, yyyy 'at' HH:mm"
    outFmt.timeZone = TimeZone.current

    let sorted = events.sorted { $0.startDate < $1.startDate }
    for event in sorted {
        let cal = event.calendar.title
        let start = outFmt.string(from: event.startDate)
        let title = event.title ?? "(no title)"
        let attendees = (event.attendees ?? []).filter { $0.participantType != .resource }
        let externalOrganizer = event.organizer.map { !$0.isCurrentUser } ?? false
        let isSolo = !externalOrganizer && (attendees.isEmpty || attendees.allSatisfy { $0.isCurrentUser })
        let flag = isSolo ? " | solo" : ""
        print("\(cal) | \(start) | \(title)\(flag)")
    }
}

sema.wait()
