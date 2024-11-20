import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AdminService {
  private apiUrl = 'http://127.0.0.1:5000/api/admin';

  constructor(private http: HttpClient) {}

  updateUserRole(userId: number, accessLevel: number, department: string): Observable<any> {
    return this.http.post(`${this.apiUrl}/user/${userId}/update_role`, {
      access_level: accessLevel,
      department: department,
    });
  }
}
