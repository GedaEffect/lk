import { Component, OnInit } from '@angular/core';
import { AdminService } from '../services/admin.service';

@Component({
  selector: 'app-admin',
  templateUrl: './admin.component.html',
  styleUrls: ['./admin.component.css'],
})
export class AdminComponent implements OnInit {
  users: any[] = []; // Список пользователей
  accessLevels = [0, 10, 20, 30, 50]; // Пример уровней доступа

  constructor(private adminService: AdminService) {}

  ngOnInit(): void {
    this.loadUsers();
  }

  loadUsers(): void {
    // Здесь нужно подключить API для получения списка пользователей
    // Временно: статический массив
    this.users = [
      { id: 1, first_name: 'Иван', last_name: 'Иванов', access_level: 10, department: 'HR' },
      { id: 2, first_name: 'Мария', last_name: 'Петрова', access_level: 20, department: 'IT' },
    ];
  }

  updateUserRole(user: any): void {
    this.adminService.updateUserRole(user.id, user.access_level, user.department).subscribe(() => {
      alert('Роль пользователя обновлена');
    });
  }
}
