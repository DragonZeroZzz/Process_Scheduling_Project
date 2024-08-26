# Process Scheduling Simulation using Python Tkinter and turtle
This project is a graphical simulation of different CPU scheduling algorithms implemented using Python's Tkinter and Turtle libraries. The simulator visualizes the execution of processes using First-Come, First-Served (FCFS), Shortest Job First (SJF), and Round Robin (RR) scheduling algorithms. This project was a part of the course CSS225 Operating System by SIIT.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Scheduling Algorithms](#scheduling-algorithms)
  - [First-Come, First-Served (FCFS)](#first-come-first-served-fcfs)
  - [Shortest Job First (SJF)](#shortest-job-first-sjf)
  - [Round Robin (RR)](#round-robin-rr)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)

## Features
- Visual representation of process scheduling using a Gantt chart.
- Simulation of FCFS, SJF (both preemptive and non-preemptive), and RR scheduling algorithms.
- Calculation and display of average waiting time, turnaround time, and response time.
- Interactive interface using Tkinter.

## Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/SorawitChok/Process-Scheduling-Simulation-Projec.git
   ```

2. **Install the required dependencies:**
   Ensure you have Python installed. No additional libraries are required as the project uses Tkinter and Turtle, which come with standard Python installations.

3. **Run the simulator:**
   ```sh
   python simulator.py
   ```

## Usage
- Launch the simulator using the command above.
- Input the process data (Process ID, Arrival Time, Burst Time).
- Select the scheduling algorithm you want to simulate (FCFS, SJF, RR).
- Click "Start Simulation" to see the visual representation of the process scheduling.

## Scheduling Algorithms
### First-Come, First-Served (FCFS)
- **Description:** The simplest scheduling algorithm, where the process that arrives first is executed first.
- **Characteristics:** Non-preemptive, straightforward but can cause long waiting times, especially if a long process arrives before shorter ones.

### Shortest Job First (SJF)
- **Description:** Executes the process with the shortest burst time first.
- **Characteristics:** Can be preemptive or non-preemptive. Minimizes average waiting time but requires accurate prediction of burst times.

### Round Robin (RR)
- **Description:** Each process is assigned a fixed time slice (quantum) and is cycled through in order until completion.
- **Characteristics:** Preemptive, suitable for time-sharing systems. Provides a balance between responsiveness and throughput.

## How It Works
The simulator takes input for process IDs, arrival times, and burst times, then simulates the chosen scheduling algorithm. The Gantt chart is drawn using Turtle graphics, and the simulation results (waiting time, turnaround time, response time) are displayed on the screen.

### Example:
- **Processes:** P1, P2, P3, P4, P5
- **Arrival Times:** 0, 2, 5, 10, 5
- **Burst Times:** 10, 5, 15, 20, 5

### Output:

- **FCFS:**
  <span align="center">
    <img src=.\img\FCFS-example.png>
  </span>
- **SJF (non-preemptive):**
- **SJF (preemptive):** 
- **RR:** 


## License
This code is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author
This repository was created by [Sorawit Chokphantavee](https://github.com/SorawitChok), [Sirawit Chokphantavee](https://github.com/SirawitC), Narinthorn Chinvorarat, and Nathanon Rookheb.
