import { Component } from '@angular/core';
import { Groups } from '../../interfaces/groups';

@Component({
  selector: 'app-recent-groups-list',
  standalone: false,
  templateUrl: './recent-groups-list.component.html',
  styleUrl: './recent-groups-list.component.css'
})
export class RecentGroupsListComponent {
   group: Groups = {
    name: "Amigo Oculto",
    date: "30/09/2002",
    numParticipants: 8
  }
}
