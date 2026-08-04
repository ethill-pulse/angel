# Halo Presentation

# Overview

- large digital asset buildout, integrating pulse software from acquisition into clear street
- a lot of new backend services, and a new front-end called Halo. Everything demo'd in the FE here has had a lot of BE buildout as well.
- **START SCREEN SHARING**
- Halo is our **INTERNAL** digital asset platform admin system, primarily built to support traders on the desk, but also admins, risk, and engineers
- Studio V2 widget framework, wanted to be easy to port features over to studio
- Will quickly go through some of these widgets to show high level features

# Market

- Executable Streaming Prices - we markup spread from liquidity providers instead of charging explicit fees
- click price, pre-fills new order form
- pre-trade risk check

# RFQ

- For large orders which would otherwise sweep the ESP book
- Allows desk to get an immediate quote for a large customer order
- DO NOT MODIFY account, 0.0001
- same pre-trade risk check

# Trade History

- For desk to view recently booked trades, they should all also exist in BK

# Manual Spot Booking

- The desk does a lot of voice deals. This allows them to enter them into the system
- Supports CSV upload if they have a report of multiple trades they need to upload (w/ a verification screen)

# Manual Options Booking

- To support the soon-to-launch digital asset options project

# Loans

- Currently used to view the loans as they are entered in a 3rd party project called Haruko, managed elsewhere

# Role Management

- Okta users, set their permissions

# Overview

- Halo was built over the last couple of months to fill a need as the digital business product has grown
- Talos & Haruko are 3rd party products we are currently using, our goal is to move eyes off those systems and into proprietary systems like Halo so that engineers can do their thing and migrate the backends away from paying 3rd party platforms to run our business.
