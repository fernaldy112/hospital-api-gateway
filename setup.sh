# Create services
curl -i -s -X POST http://localhost:8001/services --data name=pine-valley --data url='http://pine-valley:5000'
curl -i -s -X POST http://localhost:8001/services --data name=grand-oak --data url='http://grand-oak:5000'

# Create routes
curl -i -X POST http://localhost:8001/services/pine-valley/routes --data 'paths[]=/reserve' --data name=pine-valley-route
curl -i -X POST http://localhost:8001/services/grand-oak/routes --data 'paths[]=/reserve' --data name=grand-oak-route

# Create upstream service
curl -X POST http://localhost:8001/upstreams --data name=upstream

# Create upstream targets
curl -X POST http://localhost:8001/upstreams/upstream/targets --data target='pine-valley:5000'
curl -X POST http://localhost:8001/upstreams/upstream/targets --data target='grand-oak:5000'

# Update services' host
curl -X PATCH http://localhost:8001/services/pine-valley --data host='upstream'
curl -X PATCH http://localhost:8001/services/grand-oak --data host='upstream'