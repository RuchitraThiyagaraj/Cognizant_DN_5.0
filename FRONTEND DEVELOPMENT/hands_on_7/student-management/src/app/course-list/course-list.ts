import { Component, OnInit } from '@angular/core';
import { CourseService } from '../course-service';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { CourseCard } from '../course-card/course-card';

import { OnDestroy } from '@angular/core';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-course-list',
  imports: [FormsModule , CommonModule , CourseCard ],
  templateUrl: './course-list.html',
  styleUrl: './course-list.css',
})

export class CourseList implements OnInit, OnDestroy {

  //this can access the functions from courseService
  constructor(private courseService: CourseService) {}

  searchTerm='';


  courses: any[] = [];

  //subsription stores Subscription object
  private subscription!: Subscription;

  //when it is loading , display the spinner
  loading=true;

  // in typescript , ngOnInit would be called automatically without calling it manually
  ngOnInit() {
    this.loading = true;

    //this gets the data from the courseService using subscription 
    this.subscription = this.courseService.getCourses()
      .subscribe(data => {
        console.log(data);
        this.courses = data;
        this.loading = false;
      });}

      ngOnDestroy() {
        this.subscription.unsubscribe();
      }


}