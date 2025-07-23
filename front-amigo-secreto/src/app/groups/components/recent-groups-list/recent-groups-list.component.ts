import { Component, OnInit } from '@angular/core';
import { Groups } from '../../interfaces/groups';
import { recentGroups } from '../../mocks/recents-groups-mock';

@Component({
  selector: 'app-recent-groups-list',
  standalone: false,
  templateUrl: './recent-groups-list.component.html',
  styleUrl: './recent-groups-list.component.css'
})
export class RecentGroupsListComponent implements OnInit{
  groups = recentGroups;
  
  ngOnInit(){
    console.log(this.groups)
  }
}
