from engine.flappy import FlappyBird
from multiprocessing import Process, Queue

if __name__ == '__main__':

    # Create a queue to communicate between processes
    controller_queue = Queue() 
    status_queue = Queue()

    # Create a process to run the game
    background_game_process = Process(target=FlappyBird, args=(controller_queue, status_queue, ))
    background_game_process.start()

    while True:
        controller_queue.put("JUMP")
        status = status_queue.get()
        # print(status)