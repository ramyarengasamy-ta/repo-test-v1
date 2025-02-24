import sys
import time
from dataclasses import dataclass


@dataclass
class UserWithoutSlots:
    user_id: int
    name: str
    email: str
    is_active: bool

@dataclass(slots=True)
class UserWithSlots:
    user_id: int
    name: str
    email: str
    is_active: bool


def get_size(obj):
    return sys.getsizeof(obj)


user1 = UserWithoutSlots(1, "Alice", "alice@example.com", True)
user2 = UserWithSlots(1, "Alice", "alice@example.com", True)


print(f"Memory usage without slots: {get_size(user1)} bytes")
print(f"Memory usage with slots: {get_size(user2)} bytes")


NUM_USERS = 1_000_000

start_time = time.time()
users_without_slots = [UserWithoutSlots(i, f"User{i}", f"user{i}@example.com", True) for i in range(NUM_USERS)]
print(f"Time taken without slots: {time.time() - start_time:.2f} seconds")

start_time = time.time()
users_with_slots = [UserWithSlots(i, f"User{i}", f"user{i}@example.com", True) for i in range(NUM_USERS)]
print(f"Time taken with slots: {time.time() - start_time:.2f} seconds)")
