import { Component, OnInit } from '@angular/core';
import { NotificationService } from '../services/notification.service';

@Component({
  selector: 'app-notifications',
  templateUrl: './notification.component.html',
  styleUrls: ['./notification.component.css'],
})
export class NotificationComponent implements OnInit {
  notifications: any[] = [];
  unreadCount: number = 0;
  isOpen: boolean = false;

  constructor(private notificationService: NotificationService) {}

  ngOnInit(): void {
    this.loadNotifications();
  }

  loadNotifications(): void {
    const userId = Number(localStorage.getItem('userId'));
    this.notificationService.getNotifications(userId).subscribe((data) => {
      this.notifications = data;
      this.unreadCount = data.filter((n: any) => !n.is_read).length;
    });
  }

  toggleNotifications(): void {
    this.isOpen = !this.isOpen;
  }

  markAsRead(notificationId: number): void {
    this.notificationService.markAsRead(notificationId).subscribe(() => {
      this.loadNotifications();
    });
  }
}
