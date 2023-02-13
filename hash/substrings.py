def get_max_len_substring(data):
    m_sub_string = ''
    count = max_count = 0
    left, right = 0, len(data)

    for left in range(right):
        if data[left] not in m_sub_string:
            m_sub_string += data[left]
            count += 1
        else:
            index = m_sub_string.index(data[left])
            m_sub_string = m_sub_string[index + 1:] + data[left]
            count = len(m_sub_string)
        if count > max_count:
            max_count = count
    return max_count


if __name__ == '__main__':
    data_in = input()
    print(get_max_len_substring(data_in))
