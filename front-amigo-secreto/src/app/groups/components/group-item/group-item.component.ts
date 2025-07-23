import { Component, Input } from '@angular/core';
import { Groups } from '../../interfaces/groups';

@Component({
  selector: 'app-group-item',
  standalone: false,
  templateUrl: './group-item.component.html',
  styleUrl: './group-item.component.css'
})
export class GroupItemComponent {
  @Input() group!: Groups;
 
}
