import Lake
open Lake

package «marble-carver-template» where
  -- add package configuration options here

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git"

@[default_target]
lean_lib «Carving» where
  -- add library configuration options here
