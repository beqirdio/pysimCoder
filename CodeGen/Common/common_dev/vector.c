/*
COPYRIGHT (C) 2021  Dion Beqiri

This library is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public
License along with this library; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA.
*/

#include <pyblock.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>

double get_run_time(void);

void vector(int Flag, python_block *block)
{
  int i;
  double *y;
  int n = block->intPar[0]; // length of vector

  switch(Flag){
  case CG_OUT:
  case CG_INIT:
  case CG_END:
    y = (double*)block->y[0];
    for(i=0; i<n; i++) {
        y[i] = block->realPar[i]; // push all elements to single output
    }
    break;
  default:
    break;
  }
}

void print_vec(int Flag, python_block *block)
{
  int i, k, n;
  double t;
  double *u;


  switch(Flag){
  case CG_OUT:
    t = get_run_time();  // get the sample time and print it
    printf("%lf\t ",t);
    for(k=0; k<block->nin; k++){    // go to each vector input
      n = block->intPar[k];      // find vector length of specific input
      u = (double*)block->u[k];   // assign u pointer to each input
      printf("[%lf", u[0]);   // print first vector...
      for(i=1; i<n; i++) {      // ...then the rest
        printf(", %lf", u[i]);}
      printf("]\n\t\t ");  // close each vector with bracket, go to newline
    }
    printf("\n");
    break;
  case CG_INIT:
    break;
  case CG_END:
    break;
  default:
    break;
  }
}

void gain_vec(int Flag, python_block *block)
{
  int i, k, n;
  double *y, *u;
  double gain = block->realPar[0];  // Gain variable from parameter input

  switch(Flag){
  case CG_OUT:
  case CG_INIT:
  case CG_END:
    for(k=0; k<block->nin; k++){  // Go to inputs and outputs (equal amount for gain)
      n = block->intPar[k];  // find vector length for input/output port
      u = (double*)block->u[k];
      y = (double*)block->y[k];
      for(i=0; i<n; i++) {
          y[i] = u[i]*gain;   // send amplified value to corresponding output
      }
    }
    break;
  default:
    break;
  }
}
