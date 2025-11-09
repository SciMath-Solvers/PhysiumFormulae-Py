# The CLI Version! uses Asyncio!
import asyncio

async def main():
    await print("Task Finished with Return Code 0")
    force_mass_acceleration()
async def force_mass_acceleration():
    a = input("Acceleration without units, leave blank if none")
    async.sleep(1)
    f = input("Force without units, leave blank if none")
    async.sleep(1)
    m = input("Mass without units, leave blank if none")
    async.sleep(1)
    solve= int(input("What do you want to solve for (1.force,2.mass,3.accelertion)"))
    match solve:
        case 1:
            f=m*a
            print(f"{f} N")
        case 2:
            m=f/a
            print(f"{m} Kg")
        case 3:
            a=f/m
            print(f"{a} m/s/s")
            
    
    

asyncio.run(main())
