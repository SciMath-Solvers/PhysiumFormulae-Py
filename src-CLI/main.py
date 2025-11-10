# The CLI Version! uses Asyncio!
import asyncio

async def main():
    running = True
    while running:
        print("-------------Physium Formulae CLI v1.0.0-------------")
        print("[1] Solvers")
        print("[2] Formulas")
        print("[3] Exit")
        choice = input("Select an Option: ")
        running = False
    print("Task Finished with Return Code 0")
asyncio.run(main())