import pynecone as pc


config = pc.Config(
    app_name="pynecone_lib",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
