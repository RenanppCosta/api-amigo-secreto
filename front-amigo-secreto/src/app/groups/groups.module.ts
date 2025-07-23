import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { GroupsRoutingModule } from './groups-routing.module';
import { GroupsComponent } from './groups.component';
import { RecentGroupsListComponent } from './components/recent-groups-list/recent-groups-list.component';
import { GroupItemComponent } from './components/group-item/group-item.component';


@NgModule({
  declarations: [
    GroupsComponent,
    RecentGroupsListComponent,
    GroupItemComponent,
  ],
  imports: [
    CommonModule,
    GroupsRoutingModule
  ],
  exports:[
    RecentGroupsListComponent,
    GroupItemComponent
  ]
})
export class GroupsModule { }
