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

void mux(int Flag, python_block *block)
{
  int i;
  double *y, *u;
  int n = block->nin;

  switch(Flag){
  case CG_OUT:
  case CG_INIT:
  case CG_END:
    y = (double*)block->y[0];         // Go to each scalar signal input,
    for(i=0; i<n; i++){        // and send the value to the single vector output
      u = (double*)block->u[i];   // with same index
      y[i] = u[0];
    }
    break;
  default:
    break;
  }
}

void demux(int Flag, python_block *block)
{
  int i;
  double *y, *u;
  int n = block->nout;

  switch(Flag){
  case CG_OUT:
  case CG_INIT:
  case CG_END:
    u = (double*)block->u[0];  // Go to each element of the input vector
    for(i=0; i<n; i++){     // then send the value to the scalar signal
      y = (double*)block->y[i];         // with same index
      y[0] = u[i];
    }
    break;
  default:
    break;
  }
}

void sum_vec(int Flag, python_block *block)
{
  int i, k;
  double *y, *u;
  int n = block->dimIn[0];
  int m = block->nin;

  switch(Flag){
  case CG_OUT:
  case CG_INIT:
  case CG_END:
    y = (double*)block->y[0];
    for(i=0; i<n; i++){
      y[i] = 0;     // initialise output vector element to zero
      for(k=0; k<m; k++){   // Go to each input element  and add
        u = (double*)block->u[k]; //  its value to the output with same index
        y[i] += u[i];
      }
    }
    break;
  default:
    break;
  }
}

void sub_vec(int Flag, python_block *block)
{
  int i;
  double *y, *u1, *u2;
  int n = block->dimIn[0];

  switch(Flag){
  case CG_OUT:
  case CG_INIT:
  case CG_END:
    y = (double*)block->y[0];
    for(i=0; i<n; i++){
        u1 = (double*)block->u[0]; // Subtract first (top) input vector with
        u2 = (double*)block->u[1]; //  second (bottom) input vector
        y[i] = u1[i]-u2[i]; // Assign vector result to single output
    }
    break;
  default:
    break;
  }
}
