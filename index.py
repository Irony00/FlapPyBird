from engine.flappy import FlappyBird
from multiprocessing import Process, Queue

def background_game(controller_queue, status_queue):
    FlappyBird(controller_queue, status_queue)

if __name__ == '__main__':
    controller_queue = Queue() 
    status_queue = Queue()
    background_game_process = Process(target=background_game, args=(controller_queue, status_queue, ))
    background_game_process.start()
    while True:
        controller_queue.put("JUMP")
        status = status_queue.get()
        print(status)