import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QComboBox
from Solver import backtracking_solver, bfs_solver, dfs_solver ,ucs_solver

class NQueenSolverApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        
        # Input field for dimensions
        self.dimension_label = QLabel("Enter dimensions of the chessboard:")
        layout.addWidget(self.dimension_label)

        self.dimension_input = QLineEdit()
        layout.addWidget(self.dimension_input)

        # Dropdown list for algorithms
        self.algorithm_label = QLabel("Choose algorithm:")
        layout.addWidget(self.algorithm_label)

        self.algorithm_combobox = QComboBox()
        self.algorithm_combobox.addItems(["Backtracking", "BFS", "DFS","UCS"])
        layout.addWidget(self.algorithm_combobox)

        # Button to solve
        self.solve_button = QPushButton("Solve")
        self.solve_button.setStyleSheet("background-color: #4CAF50")
        self.solve_button.clicked.connect(self.solve)
        layout.addWidget(self.solve_button)
        # Button to clear text area
        self.clear_button = QPushButton("Clear")
        self.clear_button.setStyleSheet("background-color: #ff0000")
        self.clear_button.clicked.connect(self.clear_text_area)
        layout.addWidget(self.clear_button)

        # Text display for solution
        self.solution_text = QTextEdit()
        self.solution_text.setReadOnly(True)
        layout.addWidget(self.solution_text)

        self.setLayout(layout)
        self.setWindowTitle('N-Queen Solver')

    def solve(self):
        dimensions = int(self.dimension_input.text())
        algorithm_index = self.algorithm_combobox.currentIndex()
        if algorithm_index == 0:
            solution = backtracking_solver([], dimensions)
        elif algorithm_index == 1:
            solution = bfs_solver([], dimensions)
        elif algorithm_index == 2:
            solution = dfs_solver([], dimensions)
        elif algorithm_index == 3:
            solution = ucs_solver([], dimensions)
        else:
            solution = None
        
        if solution:
            self.display_solution(dimensions, solution)
        else:
            self.solution_text.setPlainText("No solution exists for the given dimensions.")

    def display_solution(self, dimensions, solution):
        self.solution_text.clear()
        for row in range(dimensions):
            line = ''
            for col in range(dimensions):
                if col == solution[row]:
                    line += '<font color="green" size=20 >&#9819;    </font> '  # Queen symbol in green color
                    # line += '♕ '  # Queen symbol
                else:
                    line += '<font size=20> □     </font> '  # Empty square symbol
            self.solution_text.append(line)

    def clear_text_area(self):
        self.solution_text.clear()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NQueenSolverApp()
    ex.show()
    sys.exit(app.exec_())

