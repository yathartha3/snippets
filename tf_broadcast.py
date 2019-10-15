#How to broadcast a transfrom:

from tf2_ros import TransformStamped
class blah:
    def __init__(self):
        self.tf_broadcaster = TransformBroadcaster(self.node_)


    def send_transform(self):
        # Fill up the static transform message
        static_transformStamped = TransformStamped()
        
        current_time = self.node_._clock.now()

        static_transformStamped.header.stamp = current_time.to_msg()
        static_transformStamped.header.frame_id = "map"
        static_transformStamped.child_frame_id = "odom"

        static_transformStamped.transform.translation.x = 0.0
        static_transformStamped.transform.translation.y = 0.0
        static_transformStamped.transform.translation.z = 0.0

        static_transformStamped.transform.rotation.x = 0.0
        static_transformStamped.transform.rotation.y = 0.0
        static_transformStamped.transform.rotation.z = 0.0
        static_transformStamped.transform.rotation.w = 1.0

        self.tf_broadcaster.sendTransform(static_transformStamped)
        print("transform sent")

