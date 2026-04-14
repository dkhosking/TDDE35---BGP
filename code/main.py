import bgpkit

# Discover the RIB file for a specific month/collector
broker = bgpkit.Broker()
items = broker.query(
    ts_start="2025-01-01T00:00:00Z",
    ts_end="2025-01-01T02:00:00Z",
    collector_id="route-views6",
    data_type="rib"
)

# Parse it
parser = bgpkit.Parser(url=items[0].url, filters={"type": "A"})
for elem in parser:
    print(elem.as_path)
