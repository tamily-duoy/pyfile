def minimize_batch(target_fn,gradient_fn,theta_0,tolerance=0.000001):
    """use gradient descent to find theta that
     minimizes target function"""
    step_size=[100,10,1,0.1,0.01,0.001,0.0001,0.00001]
    theta=theta_0
    target_fn=safe(target_fn)
    value=ttarget_fn(theta)

    while True:
        gradient=gradient_fn(theta)
        next_thetas=[step(theta,gradient,-step_size)
                     for step_size in step_sizes]

    next_theta=min(next_thetas,key=target_fn)
    next_value=target_fn(next_theta)

    if abs(value - next_value) < tolerance:
        return theta
    else:
        theta,value=next_theta,next_value



