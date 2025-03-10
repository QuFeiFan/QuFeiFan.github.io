from PIL import Image

def resize_image_custom_aspect_ratio(input_path, output_path, desired_width=None, desired_height=None):
    """
    手动指定目标尺寸并保持比例
    :param input_path: 原始图片路径
    :param output_path: 输出图片路径
    :param desired_width: 目标宽度（可选）
    :param desired_height: 目标高度（可选）
    """
    with Image.open(input_path) as img:
        original_width, original_height = img.size
        
        # 根据需求选择约束方向
        if desired_width is not None and desired_height is not None:
            # 如果同时指定了宽和高，需检查比例是否匹配
            aspect_ratio_original = original_width / original_height
            aspect_ratio_desired = desired_width / desired_height
            if abs(aspect_ratio_original - aspect_ratio_desired) < 1e-6:
                # 目标尺寸本身符合原比例，直接缩放
                img = img.resize((desired_width, desired_height), Image.Resampling.LANCZOS)
            else:
                # 不匹配时按单边约束缩放（例如以宽度为准）
                raise ValueError("指定的宽高比与原图不一致，请单独指定一个维度")
        
        elif desired_width is not None:
            # 仅约束宽度，高度按比例缩放
            scale_factor = desired_width / original_width
            new_height = int(original_height * scale_factor)
            img = img.resize((desired_width, new_height), Image.Resampling.LANCZOS)
        
        elif desired_height is not None:
            # 仅约束高度，宽度按比例缩放
            scale_factor = desired_height / original_height
            new_width = int(original_width * scale_factor)
            img = img.resize((new_width, desired_height), Image.Resampling.LANCZOS)
        
        else:
            raise ValueError("必须指定至少一个目标维度（width 或 height）")
        
        img.save(output_path, "JPEG", quality=90)

# 示例调用（将图片宽度固定为 800px，高度按比例缩放）
# resize_image_custom_aspect_ratio("PR_paper/static/images/algorithm0.jpeg", "algorithm0.jpg", desired_width=800)
resize_image_custom_aspect_ratio("PR_paper/static/images/algorithm1.jpeg", "algorithm1.jpg", desired_width=800)