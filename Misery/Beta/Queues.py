from typing import Dict as Xe
from asyncio import Queue, QueueEmpty as Senkuu


queues: Xe[int, Queue] = {}


async def put(chat_id: int, **kwargs) -> int:
    if chat_id not in queues:
        queues[chat_id] = Queue()
    await queues[chat_id].put({**kwargs})
    return queues[chat_id].qsize()


def get(chat_id: int) -> Xe[str, str]:
    if chat_id in queues:
        try:
            return queues[chat_id].get_nowait()
        except Senkuu:
            return None


def is_empty(chat_id: int) -> bool:
    if chat_id in queues:
        return queues[chat_id].empty()
    return True


def task_done(chat_id: int):
    if chat_id in queues:
        try:
            queues[chat_id].task_done()
        except ValueError:
            pass


def clear(chat_id: int):
    if chat_id in queues:
        if queues[chat_id].empty():
            raise Senkuu
        else:
            queues[chat_id].queue = []
    raise Empty