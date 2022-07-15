import snake_ai_2
env=snake_ai_2.Env(10,show_env=True)
for i in range(10):
    print(env.step())
env.close()