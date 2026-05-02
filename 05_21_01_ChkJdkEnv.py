# 05_30_ChkJdkEnv.py 핵심 내용
import jpype
jvm_path = jpype.getDefaultJVMPath()
if not jpype.isJVMStarted():
    jpype.startJVM(jvm_path)
print("🚀 JVM이 성공적으로 시작되었습니다!")