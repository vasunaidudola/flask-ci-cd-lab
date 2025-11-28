import os

def main():
    docker_image = os.environ["DOCKER_IMAGE"]

    env_content = f"""DOCKER_IMAGE={docker_image}
"""

    with open(".env", "w", encoding="utf-8") as f:
        f.write(env_content)

    print("Created .env file for Docker Compose")

if __name__ == "__main__":
    main()
