/* script.js */

document.addEventListener("DOMContentLoaded", function() {
  // Initialize dummy data (only if not already defined)
  if (!window.teachers) {
    window.teachers = [
      { name: "John Doe", gender: "Male", class: "Class A", isHead: true },
      { name: "Jane Smith", gender: "Female", class: "Class B", isHead: false }
    ];
  }
  if (!window.students) {
    window.students = [
      { name: "Alice", gender: "Female", class: "Class A" },
      { name: "Bob", gender: "Male", class: "Class B" },
      { name: "Charlie", gender: "Male", class: "Class A" }
    ];
  }
  if (!window.classes) {
    window.classes = [
      { name: "Class A", headTeacher: "John Doe", teachersCount: 1, studentsCount: 2 },
      { name: "Class B", headTeacher: "N/A", teachersCount: 1, studentsCount: 1 }
    ];
  }
  if (!window.events) window.events = [];
  if (!window.notices) window.notices = [];
  if (!window.staff) window.staff = [];
  if (!window.fees) window.fees = [];

  // If dashboard elements exist, update them
  if(document.getElementById("dashboard")){
    updateDashboard();
    initCharts();
  }
  // If teacher table exists, render teachers
  if(document.getElementById("teacherTable")){
    renderTeachers();
  }
  // If student table exists, render students
  if(document.getElementById("studentTable")){
    renderStudents();
  }
});

function updateDashboard() {
  document.getElementById("totalClasses").innerText = window.classes.length;
  document.getElementById("totalTeachers").innerText = window.teachers.length;
  document.getElementById("totalStudents").innerText = window.students.length;
  const headCount = window.teachers.filter(t => t.isHead).length;
  document.getElementById("totalHeadTeachers").innerText = headCount;
  updateCharts();
}

let teacherChart, studentChart;
function initCharts() {
  const teacherCtx = document.getElementById("teacherGenderChart").getContext("2d");
  teacherChart = new Chart(teacherCtx, {
    type: "pie",
    data: {
      labels: ["Male", "Female"],
      datasets: [{
        data: [0, 0],
        backgroundColor: ["#36A2EB", "#FF6384"]
      }]
    }
  });
  const studentCtx = document.getElementById("studentGenderChart").getContext("2d");
  studentChart = new Chart(studentCtx, {
    type: "pie",
    data: {
      labels: ["Male", "Female"],
      datasets: [{
        data: [0, 0],
        backgroundColor: ["#36A2EB", "#FF6384"]
      }]
    }
  });
  updateCharts();
}

function updateCharts() {
  if(teacherChart){
    const maleTeachers = window.teachers.filter(t => t.gender === "Male").length;
    const femaleTeachers = window.teachers.filter(t => t.gender === "Female").length;
    teacherChart.data.datasets[0].data = [maleTeachers, femaleTeachers];
    teacherChart.update();
  }
  if(studentChart){
    const maleStudents = window.students.filter(s => s.gender === "Male").length;
    const femaleStudents = window.students.filter(s => s.gender === "Female").length;
    studentChart.data.datasets[0].data = [maleStudents, femaleStudents];
    studentChart.update();
  }
}

function renderTeachers() {
  const tbody = document.querySelector("#teacherTable tbody");
  tbody.innerHTML = "";
  window.teachers.forEach((teacher, index) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${teacher.name}</td>
      <td>${teacher.gender}</td>
      <td>${teacher.class}</td>
      <td>${teacher.isHead ? "Yes" : "No"}</td>
      <td>
        <button onclick="editTeacher(${index})">Edit</button>
        <button onclick="removeTeacher(${index})">Delete</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function searchTeachers() {
  const query = document.getElementById("teacherSearch").value.toLowerCase();
  const rows = document.querySelectorAll("#teacherTable tbody tr");
  rows.forEach(row => {
    const name = row.children[0].innerText.toLowerCase();
    row.style.display = name.includes(query) ? "" : "none";
  });
}

function addTeacher() {
  const name = document.getElementById("newTeacherName").value;
  const gender = document.getElementById("newTeacherGender").value;
  const cls = document.getElementById("newTeacherClass").value;
  const isHead = document.getElementById("newTeacherHead").value === "true";
  if(name && cls) {
    window.teachers.push({ name, gender, class: cls, isHead });
    // Update or create class entry
    let classObj = window.classes.find(c => c.name === cls);
    if(classObj) {
      classObj.teachersCount += 1;
      if(isHead) {
        classObj.headTeacher = name;
      }
    } else {
      window.classes.push({
        name: cls,
        headTeacher: isHead ? name : "N/A",
        teachersCount: 1,
        studentsCount: 0
      });
    }
    renderTeachers();
    updateDashboard();
    document.getElementById("newTeacherName").value = "";
    document.getElementById("newTeacherClass").value = "";
  } else {
    alert("Please enter all required fields.");
  }
}

function removeTeacher(index) {
  if(confirm("Are you sure you want to delete this teacher?")){
    const teacher = window.teachers[index];
    let classObj = window.classes.find(c => c.name === teacher.class);
    if(classObj) {
      classObj.teachersCount = Math.max(0, classObj.teachersCount - 1);
      if(teacher.isHead && classObj.headTeacher === teacher.name) {
        classObj.headTeacher = "N/A";
      }
    }
    window.teachers.splice(index, 1);
    renderTeachers();
    updateDashboard();
  }
}

function editTeacher(index) {
  const teacher = window.teachers[index];
  const newName = prompt("Edit name:", teacher.name);
  if(newName !== null){
    teacher.name = newName;
    renderTeachers();
    updateDashboard();
  }
}

function renderStudents() {
  const tbody = document.querySelector("#studentTable tbody");
  tbody.innerHTML = "";
  window.students.forEach((student, index) => {
    const tr = document.createElement("tr");
    tr.innerHTML = `
      <td>${student.name}</td>
      <td>${student.gender}</td>
      <td>${student.class}</td>
      <td>
        <button onclick="editStudent(${index})">Edit</button>
        <button onclick="removeStudent(${index})">Delete</button>
      </td>
    `;
    tbody.appendChild(tr);
  });
}

function searchStudents() {
  const query = document.getElementById("studentSearch").value.toLowerCase();
  const rows = document.querySelectorAll("#studentTable tbody tr");
  rows.forEach(row => {
    const name = row.children[0].innerText.toLowerCase();
    row.style.display = name.includes(query) ? "" : "none";
  });
}

function addStudent() {
  const name = document.getElementById("newStudentName").value;
  const gender = document.getElementById("newStudentGender").value;
  const cls = document.getElementById("newStudentClass").value;
  if(name && cls) {
    window.students.push({ name, gender, class: cls });
    let classObj = window.classes.find(c => c.name === cls);
    if(classObj) {
      classObj.studentsCount += 1;
    } else {
      window.classes.push({
        name: cls,
        headTeacher: "N/A",
        teachersCount: 0,
        studentsCount: 1
      });
    }
    renderStudents();
    updateDashboard();
    document.getElementById("newStudentName").value = "";
    document.getElementById("newStudentClass").value = "";
  } else {
    alert("Please enter all required fields.");
  }
}

function removeStudent(index) {
  if(confirm("Are you sure you want to delete this student?")){
    const student = window.students[index];
    let classObj = window.classes.find(c => c.name === student.class);
    if(classObj) {
      classObj.studentsCount = Math.max(0, classObj.studentsCount - 1);
    }
    window.students.splice(index, 1);
    renderStudents();
    updateDashboard();
  }
}

function editStudent(index) {
  const student = window.students[index];
  const newName = prompt("Edit name:", student.name);
  if(newName !== null){
    student.name = newName;
    renderStudents();
    updateDashboard();
  }
}

/* Toggle Dark/Light Theme */
function toggleTheme() {
  document.body.classList.toggle("dark-theme");
}
