import subprocess
import time

N = 100

start = time.time()

for i in range(N):

    subprocess.run(
        ["dig","google.com","@127.0.0.1","-p","8053"],
        stdout=subprocess.DEVNULL
    )

end = time.time()

print("Total queries:", N)

print("Total time:", end-start)

print("Queries per second:", N/(end-start))
