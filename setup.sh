# Create upstream service
curl -X POST http://localhost:8001/upstreams --data name=upstream

# Create upstream targets
curl -X POST http://localhost:8001/upstreams/upstream/targets --data target='pine-valley:5000'
curl -X POST http://localhost:8001/upstreams/upstream/targets --data target='grand-oak:5000'

# Create services
curl -i -s -X POST http://localhost:8001/services --data name=hospital --data host='upstream'

# Create routes
curl -i -X POST http://localhost:8001/services/hospital/routes --data 'paths[]=/' --data name=hospital-route