set -e
BASE=http://localhost:18082
T=mktdata.mark_price.HYPL.PERP.BTC-USDC-USDC
G=hypl-markprice-scan-$$
OUT=/private/tmp/claude-502/-Users-ethill-workspace-repos-pulse/2f6e1f81-b228-4e4c-ab1d-68e10afbb983/scratchpad/records.jsonl
: > "$OUT"

curl -s -X POST -H "Content-Type: application/vnd.kafka.v2+json" \
  --data '{"name":"c1","format":"binary","auto.offset.reset":"earliest","fetch.min.bytes":"1","consumer.request.timeout.ms":"2000"}' \
  "$BASE/consumers/$G" > /dev/null

I="$BASE/consumers/$G/instances/c1"
trap 'curl -s -X DELETE -H "Content-Type: application/vnd.kafka.v2+json" "$I" > /dev/null' EXIT

curl -s -X POST -H "Content-Type: application/vnd.kafka.v2+json" \
  --data "{\"partitions\":[{\"topic\":\"$T\",\"partition\":0}]}" "$I/assignments"
curl -s -X POST -H "Content-Type: application/vnd.kafka.v2+json" \
  --data "{\"partitions\":[{\"topic\":\"$T\",\"partition\":0}]}" "$I/positions/beginning"

empty=0
for i in $(seq 1 400); do
  n=$(curl -s -m 30 -H "Accept: application/vnd.kafka.binary.v2+json" \
      "$I/records?timeout=3000&max_bytes=5000000" \
      | jq -c '.[]' | tee -a "$OUT" | wc -l | tr -d ' ')
  if [ "$n" = "0" ]; then empty=$((empty+1)); else empty=0; fi
  [ "$empty" -ge 3 ] && break
done
wc -l < "$OUT"
