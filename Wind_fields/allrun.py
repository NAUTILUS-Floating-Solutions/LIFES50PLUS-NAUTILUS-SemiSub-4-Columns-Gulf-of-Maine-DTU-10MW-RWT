import os
from pathlib import Path
from concurrent.futures import ProcessPoolExecutor
from itertools import repeat


def run_turbsim(inpfile: Path, turbsim_exe: Path):
    print(f"Running {inpfile}")
    os.system(f'{turbsim_exe} {inpfile} > {inpfile.with_suffix(".log")}')


if __name__ == "__main__":
    n_procs = 8
    turbsim_exe = Path(__file__).parent.parent.resolve() / "bin" / "TurbSim64.exe"
    inp_files = Path(__file__).parent.resolve().glob("*.inp")

    with ProcessPoolExecutor(max_workers=n_procs) as executor:
        executor.map(run_turbsim, inp_files, repeat(turbsim_exe))
