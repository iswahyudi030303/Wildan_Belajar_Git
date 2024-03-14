class TaskManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskManager, cls).__new__(cls)
            # Inisialisasi atribut dan metode lainnya di sini
        return cls._instance

    # Fungsionalitas lainnya
