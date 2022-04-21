VERSION=0.0.1
OWNER=javavolker
PROJECT=kubernetes-fastapi
build:
	docker build -t $(OWNER)/$(PROJECT):$(VERSION) .
run:
	docker run --rm=true -p 8080:8080 --name $(PROJECT) $(OWNER)/kubernetes-fastapi:$(VERSION)
dockerLogin:
	docker login --username $(OWNER)
push:
	docker push $(OWNER)/$(PROJECT):$(VERSION)
