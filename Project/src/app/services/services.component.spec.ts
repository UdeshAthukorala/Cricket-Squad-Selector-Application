import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { tstComponent } from './tst.component';

describe('tstComponent', () => {
  let component: tstComponent;
  let fixture: ComponentFixture<tstComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ tstComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(tstComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

