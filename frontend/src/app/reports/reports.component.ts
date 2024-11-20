import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-reports',
  templateUrl: './reports.component.html',
  styleUrls: ['./reports.component.css'],
})
export class ReportsComponent implements OnInit {
  reports: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.loadReports();
  }

  loadReports(): void {
    const department = 'HR'; // Пример: статический отдел
    this.http.get(`http://127.0.0.1:5000/api/reports/department/${department}/monthly_report`)
      .subscribe((data: any) => {
        this.reports = data;
      });
  }
}
