def process_users(users: list[str]) -> dict[str, int]:
    return {user: len(user) for user in users}



def scale_score(score: int | float) -> float | int:
    return score * 2


print(scale_score())


def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Алексей"

    return None
