output = """
                                       mohh@SERENiTY
 MMMMMMMMMMMMMMMMMMMMMMMMMmds+.        OS: Mint 19 tara
 MMm----::-://////////////oymNMd+'     Kernel: x86_64 Linux 4.15.0-34-generic
 MMd      /++                -sNMd:    Uptime: 1d 4m
 MMNso/'  dMM    '.::-. .-::.' .hMN:   Packages: 2351
 ddddMMh  dMM   :hNMNMNhNMNMNh: 'NMm   Shell: zsh 5.4.2
     NMm  dMM  .NMN/-+MMM+-/NMN' dMM   Resolution: 1366x768
     NMm  dMM  -MMm  'MMM   dMM. dMM   DE: Cinnamon 3.8.9
     NMm  dMM  -MMm  'MMM   dMM. dMM   WM: Muffin
     NMm  dMM  .mmd  'mmm   yMM. dMM   WM Theme: Linux Mint (Mint-Y)
     NMm  dMM'  ..'   ...   ydm. dMM   GTK Theme: Mint-Y [GTK2/3]
     hMM- +MMd/-------...-:sdds  dMM   Icon Theme: Mint-Y
     -NMm- :hNMNNNmdddddddddy/'  dMM   Font: Noto Sans 9
      -dMNs-''-::::-------.''    dMM   CPU: AMD A10-7400P Radeon R6, 10 Compute Cores 4C+6G @ 4x 2.5GHz [101.0°C]
       '/dMNmy+/:-------------:/yMMM   GPU: AMD KAVERI (DRM 2.50.0 / 4.15.0-34-generic, LLVM 6.0.0)
          ./ydNMMMMMMMMMMMMMMMMMMMMM   RAM: 1886MiB / 6915MiB
             \.MMMMMMMMMMMMMMMMMMM    
"""

SKIP_GRAPHIC=38
def sysinfo_scrape(output):
    """Scrapes the output from screenfetch and returns a dictionary"""
    lines=output.strip().splitlines()

    result= {}
    result['Name']=lines[0].strip().split()[-1]

    for line in lines[1:]:
        key_raw, value_raw = tuple(line.rsplit(':',1))
        # print(f'{key_raw=}, {value_raw=}')
        key = key_raw.rsplit(' ',1)[-1]
        value = value_raw.strip()
        # print(f'{key=}, {value=}')
        if key:
            result[key] = value
    return result


mac = """
                -/+:.          ejo@BlackOil
               :++++.          OS: 64bit Mac OS X 10.13.6 17G65
              /+++/.           Kernel: x86_64 Darwin 17.7.0
      .:-::- .+/:-''.::-       Uptime: 1d 49m
   .:/++++++/::::/++++++/:'    Packages: 236
 .:///////////////////////:'   Shell: bash 4.4.23
 ////////////////////////'     Resolution: 2560x1600
-+++++++++++++++++++++++'      DE: Aqua
/++++++++++++++++++++++/       WM: Quartz Compositor
/sssssssssssssssssssssss.      WM Theme: Blue
:ssssssssssssssssssssssss-     Font: SourceCodePro-Medium
 osssssssssssssssssssssssso/'  CPU: Intel Core i7-4980HQ @ 2.80GHz
 'syyyyyyyyyyyyyyyyyyyyyyyy+'  GPU: Intel Iris Pro / NVIDIA GeForce GT 750M
  'ossssssssssssssssssssss/    RAM: 9960MiB / 16384MiB
    :ooooooooooooooooooo+.    
     ':+oo+/:-..-:/+o+/-      
"""

print(sysinfo_scrape(mac))