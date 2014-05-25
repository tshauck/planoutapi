
PORT:=0.0.0.0:8999

run:
	docker run -i -t -p $(PORT):8999 --link postgresql:db thauck/planoutapi bash

