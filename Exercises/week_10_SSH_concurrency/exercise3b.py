# Instead of waiting for all of the futures to complete, use "as_completed" to print the future results as they come available. Reuse your "ssh_command2" function to accomplish this. 
# Once again use the concurrent futures "ThreadPoolExecutor" and print the "show version" results to standard output. Additionally, print the total execution time to standard output.

from concurrent.futures import ThreadPoolExecutor, as_completed
import time
from my_devices import network_devices
from my_functions import ssh_command2

def main():
    """
    Use concurrent futures threading to simultaneously gather "show version" output from devices.
    Wait for all threads to complete. Record the amount of time required to do this.
    """   
    start_time = time.time()
    max_threads = 5

    # Create the thread pool
    pool = ThreadPoolExecutor(max_threads)

    # Create list to append threads to
    futures = []
    for device in network_devices:
        futures.append(pool.submit(ssh_command2, device, "show version"))

    print("\n\n")
    for future in as_completed(futures):
        print("-" * 40)
        print("Result: " + future.result())
        print("-" * 40)
        print("\n\n")

    end_time = time.time()
    print(f"Finished in {end_time - start_time:.2f}")
    print("\n\n")

if __name__ == "__main__":
    main()