from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/judge', methods=['POST'])
def judge_code():
    data = request.get_json()
    language = data['language']
    code = data['code']
    input_data = data['input']
    expected_output = data['output']

    # 根据语言类型确定执行方式
    if language == 'Python':
        return judge_python(code, input_data, expected_output)
    elif language == 'C':
        return judge_c(code, input_data, expected_output)
    elif language == 'Java':
        return judge_java(code, input_data, expected_output)
    elif language == 'C++':
        return judge_cpp(code, input_data, expected_output)
    else:
        return jsonify({'result': 'Unsupported Language'})

def judge_python(code, input_data, expected_output):
    # 将 Python 代码写入文件
    with open('solution.py', 'w') as f:
        f.write(code)

    # 执行 Python 代码并获取输出
    try:
        result = subprocess.run(['python', 'solution.py'], input=input_data, capture_output=True, text=True, timeout=5)
        output = result.stdout.strip()
        
        # 判断输出是否符合预期
        if output == expected_output:
            return jsonify({'result': 'Accepted'})
        else:
            return jsonify({'result': 'Wrong Answer'})
    except subprocess.TimeoutExpired:
        return jsonify({'result': 'Time Limit Exceeded'})
    except Exception as e:
        return jsonify({'result': 'Error', 'message': str(e)})

def judge_c(code, input_data, expected_output):
    # 将 C 代码写入文件
    with open('solution.c', 'w') as f:
        f.write(code)

    # 编译 C 代码
    compile_result = subprocess.run(['gcc', '-o', 'solution', 'solution.c'], capture_output=True)
    if compile_result.returncode != 0:
        return jsonify({'result': 'Compile Error', 'message': compile_result.stderr.decode()})
    
    # 执行 C 代码并获取输出
    try:
        result = subprocess.run(['./solution'], input=input_data, capture_output=True, text=True, timeout=5)
        output = result.stdout.strip()
        
        # 判断输出是否符合预期
        if output == expected_output:
            return jsonify({'result': 'Accepted'})
        else:
            return jsonify({'result': 'Wrong Answer'})
    except subprocess.TimeoutExpired:
        return jsonify({'result': 'Time Limit Exceeded'})
    except Exception as e:
        return jsonify({'result': 'Error', 'message': str(e)})

def judge_java(code, input_data, expected_output):
    # 将 Java 代码写入文件
    with open('Solution.java', 'w') as f:
        f.write(code)

    # 编译 Java 代码
    compile_result = subprocess.run(['javac', 'Solution.java'], capture_output=True)
    if compile_result.returncode != 0:
        return jsonify({'result': 'Compile Error', 'message': compile_result.stderr.decode()})
    
    # 执行 Java 代码并获取输出
    try:
        result = subprocess.run(['java', 'Solution'], input=input_data, capture_output=True, text=True, timeout=5)
        output = result.stdout.strip()
        
        # 判断输出是否符合预期
        if output == expected_output:
            return jsonify({'result': 'Accepted'})
        else:
            return jsonify({'result': 'Wrong Answer'})
    except subprocess.TimeoutExpired:
        return jsonify({'result': 'Time Limit Exceeded'})
    except Exception as e:
        return jsonify({'result': 'Error', 'message': str(e)})

def judge_cpp(code, input_data, expected_output):
    # 将 C++ 代码写入文件
    with open('solution.cpp', 'w') as f:
        f.write(code)

    # 编译 C++ 代码
    compile_result = subprocess.run(['g++', '-o', 'solution', 'solution.cpp'], capture_output=True)
    if compile_result.returncode != 0:
        return jsonify({'result': 'Compile Error', 'message': compile_result.stderr.decode()})
    
    # 执行 C++ 代码并获取输出
    try:
        result = subprocess.run(['./solution'], input=input_data, capture_output=True, text=True, timeout=5)
        output = result.stdout.strip()
        
        # 判断输出是否符合预期
        if output == expected_output:
            return jsonify({'result': 'Accepted'})
        else:
            return jsonify({'result': 'Wrong Answer'})
    except subprocess.TimeoutExpired:
        return jsonify({'result': 'Time Limit Exceeded'})
    except Exception as e:
        return jsonify({'result': 'Error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
