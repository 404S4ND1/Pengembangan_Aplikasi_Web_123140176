// === CLASS untuk Data Manager ===
class DashboardManager {
  constructor(key) {
    this.key = key;
  }

  getData = () => JSON.parse(localStorage.getItem(this.key)) || [];
  saveData = (data) => localStorage.setItem(this.key, JSON.stringify(data));
}

// === Inisialisasi ===
const scheduleManager = new DashboardManager("schedules");
const taskManager = new DashboardManager("tasks");
const notesKey = "notes";

// === Render Function (Arrow + Template Literals) ===
const renderList = (data, element, type) => {
  element.innerHTML = data.map((item, index) =>
    `<div class="item">${item} 
      <button onclick="deleteItem('${type}', ${index})">Hapus</button>
    </div>`
  ).join("");
};

// === Tampilkan Jam (Async/Await Contoh Asinkron) ===
const updateClock = async () => {
  const now = new Date();
  const timeString = now.toLocaleTimeString("id-ID");
  document.getElementById("clock").textContent = `⏰ ${timeString}`;
};
setInterval(updateClock, 1000);

// === Load Data dari localStorage ===
const loadDashboard = () => {
  renderList(scheduleManager.getData(), document.getElementById("schedule-list"), "schedule");
  renderList(taskManager.getData(), document.getElementById("task-list"), "task");
  document.getElementById("notes").value = localStorage.getItem(notesKey) || "";
};

// === Tambah Data (Arrow Function) ===
const addItem = (type) => {
  const input = document.getElementById(`${type}-input`);
  const value = input.value.trim();
  if (!value) return alert("Isi dulu ya!");
  const manager = type === "schedule" ? scheduleManager : taskManager;
  const data = manager.getData();
  data.push(value);
  manager.saveData(data);
  input.value = "";
  loadDashboard();
};

// === Hapus Data ===
const deleteItem = (type, index) => {
  const manager = type === "schedule" ? scheduleManager : taskManager;
  const data = manager.getData();
  data.splice(index, 1);
  manager.saveData(data);
  loadDashboard();
};

// === Simpan Catatan ===
document.getElementById("save-notes").addEventListener("click", () => {
  localStorage.setItem(notesKey, document.getElementById("notes").value);
  alert("Catatan disimpan!");
});

// === Event Listener ===
document.getElementById("add-schedule").addEventListener("click", () => addItem("schedule"));
document.getElementById("add-task").addEventListener("click", () => addItem("task"));

// === Inisialisasi Awal ===
loadDashboard();
updateClock();
