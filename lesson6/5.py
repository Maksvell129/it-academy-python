def example(a, b, *args, **kwargs):
    print(f"{a=}")
    print(f"{b=}")
    print(f"{args=}")
    print(f"{kwargs=}")


example("Aleks",2,3,4,"age",6, (90, 80), name="test", year=2001)