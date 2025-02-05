# IT Ticket Dashboard

![IT Ticket Dashboard](https://via.placeholder.com/1000x400?text=IT+Ticket+Dashboard)

## 📌 Project Overview
The **IT Ticket Dashboard** is a web-based application designed to streamline IT support operations. It provides a structured system for logging, tracking, and resolving technical issues within an organization. The dashboard is built using **Vite** for efficient development, offering a sleek and responsive UI for IT teams and employees.

## 🚀 Features
- **Dynamic Ticket Management**: Create, update, and close tickets seamlessly.
- **User Authentication**: Secure login system for IT staff and employees.
- **Real-time Updates**: Instant status updates for ongoing IT issues.
- **Role-based Access Control**: Admin and User roles with different privileges.
- **Search & Filtering**: Quickly find tickets using keywords or status filters.
- **Dashboard Analytics**: Visual representation of ticket statistics.
- **Responsive Design**: Optimized for desktops, tablets, and mobile devices.

## 🛠️ Tech Stack
| Technology | Description |
|------------|------------|
| **Vite** | Fast and modern frontend build tool |
| **React.js** | Component-based UI development |
| **Tailwind CSS** | Utility-first CSS framework for styling |
| **Express.js** | Backend framework for API handling |
| **MongoDB** | NoSQL database for ticket storage |
| **JWT Authentication** | Secure authentication mechanism |
| **Socket.io** | Real-time ticket updates |

## 📂 Project Structure
```
IT_Ticket_Dashboard/
│── src/
│   ├── components/       # Reusable UI components
│   ├── pages/            # Dashboard pages
│   ├── assets/           # Images, icons, and static assets
│   ├── utils/            # Helper functions
│   ├── services/         # API requests & authentication
│── public/               # Static files
│── server/               # Backend API using Express
│── .env                  # Environment variables
│── package.json          # Project dependencies
│── vite.config.js        # Vite configuration
│── README.md             # Project documentation
```

## 🔧 Installation & Setup
### Prerequisites
Ensure you have the following installed:
- [Node.js](https://nodejs.org/) (LTS recommended)
- [MongoDB](https://www.mongodb.com/)
- [Git](https://git-scm.com/)

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/WiseTechLTS/Wcjc_IT_Tech_Capstone.git
cd Wcjc_IT_Tech_Capstone/it_ticket_dashboard
```

### 2️⃣ Install Dependencies
```sh
npm install
```

### 3️⃣ Configure Environment Variables
Create a `.env` file and add your credentials:
```sh
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_secret_key
PORT=5000
```

### 4️⃣ Start the Development Server
```sh
npm run dev
```

### 5️⃣ Start the Backend Server
```sh
cd server
npm start
```

## 🖥️ Usage
1. Open the dashboard in your browser (`http://localhost:5173` by default).
2. Login or register to access the ticket system.
3. Submit new tickets and track progress in real time.
4. IT admins can manage tickets, assign them, and resolve issues.

## 📸 Screenshots
### 🎟️ Ticket Management
![Ticket Management](https://via.placeholder.com/800x400?text=Ticket+Management)
### 📊 Dashboard View
![Dashboard](https://via.placeholder.com/800x400?text=Dashboard)

## 📜 License
This project is licensed under the [MIT License](LICENSE).

## 🤝 Contributing
Contributions are welcome! Follow these steps:
1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes and push to your fork.
4. Submit a pull request.

## 📬 Contact
For questions or suggestions, reach out via:
- **GitHub Issues**: [Open an Issue](https://github.com/WiseTechLTS/Wcjc_IT_Tech_Capstone/issues)
- **Email**: [support@wisetechlts.com](mailto:support@wisetechlts.com)

---
✨ Developed by **WiseTech LTS** | 🚀 Version 1.0.0
