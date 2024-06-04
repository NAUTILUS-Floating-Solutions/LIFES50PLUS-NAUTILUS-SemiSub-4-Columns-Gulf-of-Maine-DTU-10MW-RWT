import os
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat


def run_fast(fstfile: Path, fast_exe: Path):
    print(f"Running {fstfile}")
    os.chdir(fstfile.parent.resolve())
    os.system(f'{fast_exe} {fstfile} > {fstfile.with_suffix(".log")}')


if __name__ == "__main__":
    n_procs = 8
    turbsim_exe = Path(__file__).parent.parent.resolve() / "bin" / "FAST_Win32.exe"
    fast_cases = Path(__file__).parent.resolve().glob("*_*")
    fst_files = [fast_case / "DTU_10MW_NAUTILUS_GoM.fst" for fast_case in fast_cases]

    with ProcessPoolExecutor(max_workers=n_procs) as executor:
        executor.map(run_fast, fst_files, repeat(turbsim_exe))
