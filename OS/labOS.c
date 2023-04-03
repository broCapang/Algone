#include <stdio.h>

// TODO : TURNAROUND TIME, WAITING TIME IN A TABLE


// Define a struct to represent a process
typedef struct {
    int pid;      // Process ID
    int burst;    // Burst time (in CPU cycles)
    int arrival;  // Arrival time (in CPU cycles)
} Process;

int main() {
    int n;  // Number of processes
    printf("Enter the number of processes: ");
    scanf("%d", &n);

    // Initialize an array of processes
    Process processes[n];
    for (int i = 0; i < n; i++) {
        printf("Enter the burst time of process %d: ", i+1);
        scanf("%d", &processes[i].burst);
        processes[i].arrival = i;  // Use process index as arrival time
        processes[i].pid = i+1;
    }

    // Sort the processes in order of arrival time (using bubble sort)
    for (int i = 0; i < n-1; i++) {
        for (int j = 0; j < n-i-1; j++) {
            if (processes[j].arrival > processes[j+1].arrival) {
                Process temp = processes[j];
                processes[j] = processes[j+1];
                processes[j+1] = temp;
            }
        }
    }

    // Simulate the FCFS scheduling algorithm
    int curr_time = 0;  // Current time (in CPU cycles)
    printf("\nExecution sequence: ");
    for (int i = 0; i < n; i++) {
        curr_time += processes[i].burst;  // Update current time
        printf("P%d ", processes[i].pid);  // Print process ID
    }

    // Calculate average waiting time
    float total_wait = 0;
    for (int i = 0; i < n; i++) {
        total_wait += (curr_time - processes[i].arrival - processes[i].burst);
    }
    float avg_wait = total_wait / n;

    // Print the average waiting time
    printf("\nAverage waiting time: %.2f\n", avg_wait);

    return 0;
}
