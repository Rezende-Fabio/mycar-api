from api import create_app

if __name__ == "__main__":
    api = create_app()
    api.run()