document.addEventListener('DOMContentLoaded', () => {
    // === DOM Elements ===
    const taskForm = document.getElementById('task-form');
    const taskIdInput = document.getElementById('task-id');
    const taskNameInput = document.getElementById('task-name');
    const taskCourseInput = document.getElementById('task-course');
    const taskDeadlineInput = document.getElementById('task-deadline');
    const submitButton = document.getElementById('submit-button');
    const cancelEditButton = document.getElementById('cancel-edit-button');
    const taskList = document.getElementById('task-list');
    const incompleteCountSpan = document.getElementById('incomplete-count');
    const searchInput = document.getElementById('search-input');
    const filterStatus = document.getElementById('filter-status');

    // === Application State ===
    let tasks = JSON.parse(localStorage.getItem('tasks')) || [];
    let isEditing = false;

    // === Functions ===

    /**
     * Menyimpan array tasks ke localStorage
     */
    const saveTasks = () => {
        localStorage.setItem('tasks', JSON.stringify(tasks));
    };

    /**
     * Merender daftar tugas ke DOM berdasarkan filter dan pencarian
     */
    const renderTasks = () => {
        taskList.innerHTML = '';

        // Terapkan filter dan pencarian
        const searchValue = searchInput.value.toLowerCase();
        const filterValue = filterStatus.value;

        const filteredTasks = tasks.filter(task => {
            const matchesSearch = task.course.toLowerCase().includes(searchValue);
            const matchesFilter = 
                filterValue === 'all' ||
                (filterValue === 'completed' && task.isCompleted) ||
                (filterValue === 'incomplete' && !task.isCompleted);
            return matchesSearch && matchesFilter;
        });

        if (filteredTasks.length === 0) {
            taskList.innerHTML = '<p style="text-align: center; color: #888;">Tidak ada tugas ditemukan.</p>';
        } else {
            filteredTasks.forEach(task => {
                const taskItem = document.createElement('div');
                taskItem.className = `task-item ${task.isCompleted ? 'completed' : ''}`;
                taskItem.dataset.id = task.id;

                taskItem.innerHTML = `
                    <div class="task-details">
                        <p>${task.name}</p>
                        <p><strong>Mata Kuliah:</strong> <span>${task.course}</span></p>
                        <p><strong>Deadline:</strong> ${new Date(task.deadline).toLocaleDateString('id-ID')}</p>
                    </div>
                    <div class="task-actions">
                        <button class="btn-complete">${task.isCompleted ? 'Batal Selesai' : 'Selesai'}</button>
                        <button class="btn-edit">Edit</button>
                        <button class="btn-delete">Hapus</button>
                    </div>
                `;
                taskList.appendChild(taskItem);
            });
        }
        updateStats();
    };

    /**
     * Memperbarui jumlah tugas yang belum selesai
     */
    const updateStats = () => {
        const incompleteCount = tasks.filter(task => !task.isCompleted).length;
        incompleteCountSpan.textContent = incompleteCount;
    };

    /**
     * Menampilkan pesan error pada form
     */
    const showValidationError = (elementId, message) => {
        const errorElement = document.getElementById(elementId);
        errorElement.textContent = message;
    };

    /**
     * Menghapus semua pesan error pada form
     */
    const clearValidationErrors = () => {
        document.querySelectorAll('.error-message').forEach(el => el.textContent = '');
    };

    /**
     * Memvalidasi input form
     */
    const validateForm = () => {
        clearValidationErrors();
        let isValid = true;
        const today = new Date().toISOString().split('T')[0];

        if (!taskNameInput.value.trim()) {
            showValidationError('name-error', 'Nama tugas tidak boleh kosong.');
            isValid = false;
        }
        if (!taskCourseInput.value.trim()) {
            showValidationError('course-error', 'Mata kuliah tidak boleh kosong.');
            isValid = false;
        }
        if (!taskDeadlineInput.value) {
            showValidationError('deadline-error', 'Deadline harus diisi.');
            isValid = false;
        } else if (taskDeadlineInput.value < today && !isEditing) {
             // Validasi tanggal lampau hanya untuk tugas baru
            showValidationError('deadline-error', 'Deadline tidak boleh tanggal yang sudah lewat.');
            isValid = false;
        }
        return isValid;
    };

    /**
     * Mengatur ulang form ke kondisi awal
     */
    const resetForm = () => {
        taskForm.reset();
        taskIdInput.value = '';
        isEditing = false;
        submitButton.textContent = 'Tambah Tugas';
        cancelEditButton.classList.add('hidden');
        clearValidationErrors();
    };

    // === Event Listeners ===

    /**
     * Handle submit form untuk menambah atau mengedit tugas
     */
    taskForm.addEventListener('submit', (e) => {
        e.preventDefault();
        if (!validateForm()) return;

        const taskData = {
            id: isEditing ? taskIdInput.value : Date.now().toString(),
            name: taskNameInput.value.trim(),
            course: taskCourseInput.value.trim(),
            deadline: taskDeadlineInput.value,
            isCompleted: false
        };

        if (isEditing) {
            // Update tugas yang ada
            const taskIndex = tasks.findIndex(t => t.id === taskData.id);
            // Pertahankan status 'isCompleted' yang sudah ada
            taskData.isCompleted = tasks[taskIndex].isCompleted; 
            tasks[taskIndex] = taskData;
        } else {
            // Tambah tugas baru
            tasks.push(taskData);
        }

        saveTasks();
        renderTasks();
        resetForm();
    });

    /**
     * Handle klik pada daftar tugas (delegasi event)
     */
    taskList.addEventListener('click', (e) => {
        const taskItem = e.target.closest('.task-item');
        if (!taskItem) return;

        const taskId = taskItem.dataset.id;
        const taskIndex = tasks.findIndex(t => t.id === taskId);

        if (e.target.classList.contains('btn-delete')) {
            tasks.splice(taskIndex, 1);
            saveTasks();
            renderTasks();
        } else if (e.target.classList.contains('btn-complete')) {
            tasks[taskIndex].isCompleted = !tasks[taskIndex].isCompleted;
            saveTasks();
            renderTasks();
        } else if (e.target.classList.contains('btn-edit')) {
            const taskToEdit = tasks[taskIndex];
            isEditing = true;
            taskIdInput.value = taskToEdit.id;
            taskNameInput.value = taskToEdit.name;
            taskCourseInput.value = taskToEdit.course;
            taskDeadlineInput.value = taskToEdit.deadline;
            
            submitButton.textContent = 'Update Tugas';
            cancelEditButton.classList.remove('hidden');
            taskNameInput.focus();
        }
    });

    /**
     * Handle tombol batal edit
     */
    cancelEditButton.addEventListener('click', resetForm);

    /**
     * Handle filter dan pencarian
     */
    searchInput.addEventListener('input', renderTasks);
    filterStatus.addEventListener('change', renderTasks);


    // === Initial Load ===
    renderTasks();
});