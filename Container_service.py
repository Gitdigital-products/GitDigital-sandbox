import docker

client = docker.from_env()

def run_container(image, command):
    container = client.containers.run(
        image=image,
        command=command,
        detach=True
    )
    return container.id
