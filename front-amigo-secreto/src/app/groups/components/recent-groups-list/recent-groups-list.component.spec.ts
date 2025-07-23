import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RecentGroupsListComponent } from './recent-groups-list.component';

describe('RecentGroupsListComponent', () => {
  let component: RecentGroupsListComponent;
  let fixture: ComponentFixture<RecentGroupsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [RecentGroupsListComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RecentGroupsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
