# Process Scheduling Simulation using Python Tkinter and turtle
This project is a graphical simulation of different CPU scheduling algorithms implemented using Python's Tkinter and Turtle libraries. The simulator visualizes the execution of processes using First-Come, First-Served (FCFS), Shortest Job First (SJF), and Round Robin (RR) scheduling algorithms. This project was a part of the course CSS225 Operating System by SIIT.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [User Interface](#user-interface)
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

## User Interface
The user interface (UI) of the Process Scheduling Simulator is designed to be simple and intuitive, making it easy for users to input data and visualize the scheduling algorithms. It is built using Python's Tkinter library and consists of the following components:

- Input Section:
  - Process ID: A text field to input the unique identifier for each process.
  - Arrival Time: A text field to enter the time at which each process arrives in the queue.
  - Burst Time: A text field for entering the CPU burst time required by each process.

-Algorithm Selection:
  - A set of radio buttons allowing the user to choose between FCFS, SJF, and RR scheduling algorithms.

- Simulation Controls:
  - Additional Process: Buttons to add or remove the number of process to simulate. 
  - Start Simulation: A button that begins the simulation based on the entered data and selected algorithm.

- Output Section:
  -  Displays the Gantt chart representing the execution order of processes.
  -  Shows calculated metrics such as average waiting time, turnaround time, and response time.
 
This is an example of our system's user interface.

<p align="center">
  <img src=./img/User-interface.png>
</p>


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

### Output FCFS:
  <p align="center">
    <img src=.\img\FCFS-example.png>
  </p>

### Output SJF (non-preemptive):
 <p align="center">
    <img src=.\img\SJF-non-preemptive-example.png>
  </p>
  
### Output SJF (preemptive): 
 <p align="center">
    <img src=.\img\SJF-preemptive-example.png>
  </p>
  
### Output RR: 
  <p align="center">
    <img src=.\img\RR-example.png>
  </p>
  


## License
This code is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author
This repository was created by [Sorawit Chokphantavee](https://github.com/SorawitChok), [Sirawit Chokphantavee](https://github.com/SirawitC), Narinthorn Chinvorarat, and Nathanon Rookheb.
